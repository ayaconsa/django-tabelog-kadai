// ---------------------------
// ▼A：対象要素を得る
// ---------------------------
var tabs = document.getElementById('my_tabcontrol').getElementsByTagName('a');
var pages = document.getElementById('my_tabbody').getElementsByTagName('div');

// ---------------------------
// ▼B：タブの切り替え処理
// ---------------------------
function changeTab(targetid) {
  // ▼B-2. 指定のタブページだけを表示する
  for (var i = 0; i < pages.length; i++) {
    if (pages[i].id != targetid) {
      pages[i].style.display = "none";
    } else {
      pages[i].style.display = "block";
    }
  }

  // ▼B-3. クリックされたタブを前面に表示する
  for (var i = 0; i < tabs.length; i++) {
    tabs[i].style.zIndex = "0";
  }

  document.querySelector('a[href="#' + targetid + '"]').style.zIndex = "10";

  // ▼B-4. ページ遷移しないようにfalseを返す
  return false;
}

// タブクリック時の処理
for (var i = 0; i < tabs.length; i++) {
  tabs[i].onclick = function() {
    var targetid = this.href.substring(this.href.indexOf('#') + 1, this.href.length);
    window.location.hash = targetid; // ハッシュを更新
    changeTab(targetid);
    return false;
  };
}

// 初期表示のタブを設定
window.onload = function() {
  var hash = window.location.hash.substring(1);
  if (hash) {
    changeTab(hash);
  } else {
    tabs[0].onclick();
  }
};
