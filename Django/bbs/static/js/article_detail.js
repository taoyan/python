

$("#div_digg .action").click(function () {
            var username = $(".info").attr("username");
            if (username == ""){
                location.href = "/login/";
                return
            }


            //赞或者灭
            var is_up = $(this).hasClass("diggit");
            var article_id = $(".info").attr("article_id");
            $.ajax({
                url:"/blog/up_down/",
                type:"post",
                data:{
                    is_up:is_up,
                    article_id:article_id,
                    csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val()
                },
                success:function (data) {
                    // {#console.log(state)#}
                    if (data.state){
                        if (is_up){
                            var val = $("#digg_count").text();
                            $("#digg_count").text(parseInt(val) + 1);
                        }
                        else{
                            var val = $("#bury_count").text();
                            $("#bury_count").text(parseInt(val) + 1);
                        }
                    }
                    else {
                        if (data.first_action)
                        {
                            $("#digg_tips").html("您已经推荐过了");
                        }
                        else
                            $("#digg_tips").html("您已经反对过了");

                        setTimeout(function () {
                            $("#digg_tips").html("")
                        }, 1000)
                    }
                }
            })
        })