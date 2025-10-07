document.addEventListener('DOMContentLoaded', () => {
    const productList = document.getElementById('product-list');
    const form = document.getElementById('product-form');
    const nameInput = document.getElementById('name');
    const priceInput = document.getElementById('price');
    const descInput = document.getElementById('description');

    function fetchProducts() {
        fetch('/products')
            .then(res => res.json())
            .then(products => {
                productList.innerHTML = '';
                products.forEach(product => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        <div class="product-info">
                            <span class="product-name">${product.name}</span>
                            <span class="product-price">$${parseFloat(product.price).toFixed(2)}</span>
                            <span class="product-desc">${product.description || ''}</span>
                        </div>
                        <div class="actions">
                            <button class="delete-btn" data-id="${product.id}">Delete</button>
                        </div>
                    `;
                    productList.appendChild(li);
                });

                // Add delete event listeners
                document.querySelectorAll('.delete-btn').forEach(btn => {
                    btn.addEventListener('click', (e) => {
                        const id = btn.getAttribute('data-id');
                        fetch(`/products/${id}`, { method: 'DELETE' })
                            .then(() => fetchProducts());
                    });
                });
            });
    }

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = nameInput.value.trim();
        const price = priceInput.value;
        const description = descInput.value.trim();
        if (!name || !price) return;
        fetch('/products', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, price, description })
        }).then(res => {
            if (res.ok) {
                form.reset();
                fetchProducts();
            }
        });
    });

    fetchProducts();
});