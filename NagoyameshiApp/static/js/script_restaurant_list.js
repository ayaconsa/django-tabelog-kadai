
document.addEventListener('DOMContentLoaded', function() {
  // プルダウンが変更されたときにURLにクエリ情報を追加してリダイレクトする
  document.getElementById('sort-select').addEventListener('change', function() {
    var sortOption = this.value;
    var currentUrl = window.location.href;

    // クエリ文字列が既に含まれている場合
    if (currentUrl.indexOf('?') !== -1) {
      // クエリ文字列の先頭に&を追加して追加のパラメータを付け足す
      window.location.href = currentUrl + '&sort=' + sortOption;
    } else {
      // クエリ文字列が含まれていない場合
      window.location.href = currentUrl + '?sort=' + sortOption;
    }
  });
});
