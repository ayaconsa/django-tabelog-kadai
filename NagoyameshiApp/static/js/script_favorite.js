// ---------------------------
// お気に入りToggle
// ---------------------------

document.addEventListener('DOMContentLoaded', function () {
    const favoriteBtn = document.getElementById('favorite-btn');
    if (favoriteBtn) {
        favoriteBtn.addEventListener('click', function () {
            const restaurantId = this.getAttribute('data-restaurant-id');
            fetch('/toggle_favorite/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify({ restaurant_id: restaurantId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'favorited') {
                    favoriteBtn.textContent = 'お気に入り解除';
                } else if (data.status === 'unfavorited') {
                    favoriteBtn.textContent = 'お気に入り登録';
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }
});
