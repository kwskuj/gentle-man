// 初期読み込み
$(function () {
  left();
  right();
  display_control("contents_wrap", true);
  menu_button();
  new_video();
  recommend();
  rank();
  recently();
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

/**
 * ここでサーバーサイドにアクセスして
 * データベースから持ってきた画像を変数に格納して
 * タグに入れ込んで表出させてる
 * aタグはめんどかったからそのまま
 */
function new_video() {
  $.ajax({
    type: "GET",
    url: "/new_video",
  }).done(function (json) {
    var test_data = JSON.parse(json);
    console.log(test_data)
    test_data.forEach(function (val, idx) {
      var data = val
      var li_tag = $("<li>", {
        class: "li_" + "new_video" + idx
      });
      var img = $("<img>", {
        src: data,
      });
      var a_tag = $("<a>", {
        target: "_blank",
        href: "https://www.xvideos.com/embedframe/15057399",
      });
      var a_tag_img = $("<img>", {
        src: "https://static-hw.xvideos.com/v3/img/player/icon-play.svg",
      });
      a_tag.append(a_tag_img);
      li_tag.append(a_tag, img);
      $(".slideSampleThumbnail_0").append(li_tag);
    });
  });
}

function recommend() {
  $.ajax({
    type: "GET",
    url: "/recommend",
  }).done(function (json) {
    var test_data = JSON.parse(json);
    console.log(test_data)
    test_data.forEach(function (val, idx) {
      var data = val
      var li_tag = $("<li>", {
        class: "li_" + "recommend" + idx
      });
      var img = $("<img>", {
        src: data,
      });
      var a_tag = $("<a>", {
        target: "_blank",
        href: "https://www.xvideos.com/embedframe/15057399",
      });
      var a_tag_img = $("<img>", {
        src: "https://static-hw.xvideos.com/v3/img/player/icon-play.svg",
      });
      a_tag.append(a_tag_img);
      li_tag.append(a_tag, img);
      $(".slideSampleThumbnail_1").append(li_tag);
    });
  });
}

function rank() {
  $.ajax({
    type: "GET",
    url: "/rank",
  }).done(function (json) {
    var test_data = JSON.parse(json);
    console.log(test_data)
    test_data.forEach(function (val, idx) {
      var data = val
      var li_tag = $("<li>", {
        class: "li_" + "rank" + idx
      });
      var img = $("<img>", {
        src: data,
      });
      var a_tag = $("<a>", {
        target: "_blank",
        href: "https://www.xvideos.com/embedframe/15057399",
      });
      var a_tag_img = $("<img>", {
        src: "https://static-hw.xvideos.com/v3/img/player/icon-play.svg",
      });
      a_tag.append(a_tag_img);
      li_tag.append(a_tag, img);
      $(".slideSampleThumbnail_2").append(li_tag);
    });
  });
}

function recently() {
  $.ajax({
    type: "GET",
    url: "/recently",
  }).done(function (json) {
    var test_data = JSON.parse(json);
    console.log(test_data)
    test_data.forEach(function (val, idx) {
      var data = val
      var li_tag = $("<li>", {
        class: "li_" + "recently" + idx
      });
      var img = $("<img>", {
        src: data,
      });
      var a_tag = $("<a>", {
        target: "_blank",
        href: "https://www.xvideos.com/embedframe/15057399",
      });
      var a_tag_img = $("<img>", {
        src: "https://static-hw.xvideos.com/v3/img/player/icon-play.svg",
      });
      a_tag.append(a_tag_img);
      li_tag.append(a_tag, img);
      $(".slideSampleThumbnail_3").append(li_tag);
    });
  });
}

function top_page_url() {
  url();
  console.log(test_data)
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

function test02() {
  var url = ['https://www.xvideos.com/embedframe/30973485', 'https://www.xvideos.com/embedframe/16490523', 'https://www.xvideos.com/embedframe/30042231', 'https://www.xvideos.com/embedframe/30190627', 'https://www.xvideos.com/embedframe/29464917', 'https://www.xvideos.com/embedframe/17596727'];
  var a_href = "href ="+'"'+ url +'"';
  url.forEach(function (a_href, indx) {
    console.log(a_href);
    $('all-video_container_item', {
      id: 'div' + '_' + indx
    });
    var a_tag = $('<a " + a_href + "><img src="https://static-hw.xvideos.com/v3/img/player/icon-play.svg"></a>')
    $(".all-video_container_item").append(a_tag);
  });
}
// var url = "https://www.xvideos.com/embedframe/30973485";
//   var a_href = "href ="+'"'+ url +'"';
//   console.log(a_href);
//   var a_tag = $("<a " + a_href + "></a>")
//   $("html").append(a_tag)
