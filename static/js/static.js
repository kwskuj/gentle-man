$(function () {
  left();
  right();
  display_control("contents_wrap", true);
   menu_button();
   test02();
});

function test(){
      var jsonData = $.ajax({
        type: "GET",
        url: "/test",
        async: false,
    }).responseText;
    console.log(jsonData)
}

function display_control(id, is_disp) {
  var disp = is_disp ? 'block' : 'none';
  $('#' + id).css('display', disp);
}

function menu_button() {
  $(document).on('click', '#hunbergar', function () {
    a = 1
    $(this).toggleClass("on");
    if ($(this).hasClass("on")) {
      $('#main_container').css({
        "width": "80%"
      });
      display_control('side_bar', true);
    } else {
      $('#main_container').css({
        "width": "100%"
      });
      display_control('side_bar', false);
    }
  });
}
function left() {
  $(document).on('click', '.left_button', function () {
    var clone = $(this).parent("div").children("ul").children("li:first").clone(true);
    $(this).parent("div").children("ul").children("li:first").animate({
      left: -70
    }, 50000);
    $(this).parent("div").children("ul").children("li:first").remove();
    clone.clone(true).insertAfter($(this).parent("div").children("ul").children("li:last"));
  });
}

function right() {
  $(document).on('click', '.right_button', function () {
    var clone = $(this).parent("div").children("ul").children("li:last").clone(true);
    $(this).parent("div").children("ul").children("li:last").animate({
      right: -70
    }, 50000);
    $(this).parent("div").children("ul").children("li:last").remove();
    clone.clone(true).insertBefore($(this).parent("div").children("ul").children("li:first"));
  });
}

function test02(){
  var url = ['https://www.xvideos.com/embedframe/30973485','https://www.xvideos.com/embedframe/16490523','https://www.xvideos.com/embedframe/30042231','https://www.xvideos.com/embedframe/30190627','https://www.xvideos.com/embedframe/29464917','https://www.xvideos.com/embedframe/17596727'];
url.forEach(function(val,indx){
  console.log (val);
  var a_tag = $('<a href="">',{
     id:'a' + '_' + indx
   });
  var iframe = $("<object >",{
    src:val,
  });
 a_tag.append(object);
  $(".all-video_container_item" ).append(a_tag);
});



}
