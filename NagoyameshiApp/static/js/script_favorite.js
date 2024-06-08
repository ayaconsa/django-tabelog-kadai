// csrf_token 取得
function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
			const cookies = document.cookie.split(';');
			for (let i = 0; i < cookies.length; i++) {
					const cookie = cookies[i].trim();
					if (cookie.substring(0, name.length + 1) === (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
					}
			}
	}
	return cookieValue;
}

function csrfSafeMethod(method) {
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

document.addEventListener('DOMContentLoaded', function () {
	const favoriteButton = document.getElementById('favorite-btn');

	if (favoriteButton) {
			console.log('Favorite button found');
			favoriteButton.addEventListener('click', function () {
					console.log('Favorite button clicked');
					const csrf_token = getCookie("csrftoken");
					const isFavorite = this.getAttribute('data-favorite') === 'true';
					const restaurantId = this.getAttribute('data-restaurant-id');
					const url = `/favorite_toggle/${restaurantId}/`;

					fetch(url, {
							method: 'POST',
							headers: {
									'Content-Type': 'application/json',
									'X-CSRFToken': csrf_token
							},
							body: JSON.stringify({})
					})
					.then(response => {
							if (!response.ok) {
									throw new Error('Network response was not ok');
							}
							return response.json();
					})
					.then(data => {
							if (data.status === 'success') {
									console.log('Favorite status toggled');
									this.setAttribute('data-favorite', String(!isFavorite));
									if (data.favorite_status === 'unfavorited') {
											this.textContent = 'お気に入りに追加';
									} else if (data.favorite_status === 'favorited') {
											this.textContent = 'お気に入りから削除';
									}
							} else {
									alert(data.message);
							}
					})
					.catch(error => {
							console.error('Error:', error);
					});
			});
	} else {
			console.error('Favorite button not found');
	}
});
