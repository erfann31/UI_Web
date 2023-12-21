        document.getElementById('search').addEventListener('input', function() {
            let searchText = this.value.toLowerCase();
            let newsItems = document.querySelectorAll('.list-search-item');

            newsItems.forEach(function(item) {
                let newsText = item.textContent.toLowerCase();
                if (newsText.includes(searchText)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });