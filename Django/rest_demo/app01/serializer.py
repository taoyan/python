
from .models import Publisher, Book

from rest_framework import serializers
class PublisherSerializers(serializers.Serializer):
    name = serializers.CharField()
    addr = serializers.CharField()


class PublisherModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


# 手写定制
class BookSerializers(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    price = serializers.IntegerField()
    publisher = serializers.CharField(source="publisher.addr")

    # author = serializers.CharField(source="authors.all")
    authors = serializers.SerializerMethodField()

    def get_authors(self, book):
        temp = []
        for author in book.authors.all():
            temp.append(author.name)
        return temp




class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # r'^publishers/(?P<pk>\d+)/$'
    publisher = serializers.HyperlinkedIdentityField(
        view_name="publish_detail",
        lookup_field="publisher_id",
        lookup_url_kwarg="pk"
    )

    # publisher = serializers.CharField(source="publisher.pk")
    # authors = serializers.SerializerMethodField()
    #
    # def get_authors(self, book):
    #     temp = []
    #     for author in book.authors.all():
    #         temp.append(author.name)
    #     return temp

    # def create(self, validated_data):
    #     print("validated_data", validated_data)
    #     book = Book.objects.create(title=validated_data["title"], price=validated_data["price"],
    #                         publisher_id=validated_data["publisher"]["pk"])
    #     book.authors.add(*validated_data["authors"])
    #     return book

