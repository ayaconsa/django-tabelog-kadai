
// 店舗一覧ページの並び替え（ボタンを設置せず、プルダウン選択のみで実行）
document.addEventListener('DOMContentLoaded', function() {
  // プルダウンが変更されたときにフォームを送信する
  document.getElementById('sort-select').addEventListener('change', function() {
    document.getElementById('sort-form').submit();
  });
});