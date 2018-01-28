// 初期読み込み
$(function () {
  left();
  right();
  menu_button();
});
/**
 * ディスプレイコントロール
 * @param {*} id id名
 * @param {*} is_disp　trueかfalse 
 */
function display_control(id, is_disp) {
  var disp = is_disp ? 'block' : 'none';
  $('#' + id).css('display', disp);
}

function test(){
  var test;
  $.ajax({
    type: "GET",
    url: "/test",
    datatype:"json"
  }).done(function(json){
   test = JSON.parse(json);
   //console.log(test);
   console.log(test.players);
   return test;
  }).fail(function () {
    console.log("fuck")
  });
}

function test_2(){

  var test_test = test();
  //console.log(test_test)
}

/**
 * メニューボタンイベント
 */
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
/**
 * スライダー左ボタン
 */
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
/**
 * スライダー右ボタン
 */
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
