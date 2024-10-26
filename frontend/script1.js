// Function to filter grid items based on search input
function filterItems() {
    const searchInput = document.getElementById('search-bar').value.toLowerCase();
    const gridItems = document.querySelectorAll('.grid .item');

    gridItems.forEach(item => {
        const itemName = item.getAttribute('data-item').toLowerCase();
        
        // Show or hide items based on search input
        if (itemName.includes(searchInput)) {
            item.style.display = 'flex'; // Show item
        } else {
            item.style.display = 'none'; // Hide item
        }
    });
}

function addItem(itemName) {
    const cartItems = document.getElementById('cart-items');
    const quantityInput = document.querySelector(`.item[data-item='${itemName}'] .quantity`);
    const quantity = parseInt(quantityInput.value); // Get the quantity

    // Check if item is already in the cart
    const existingItem = document.querySelector(`#cart-items li[data-item='${itemName}']`);

    if (existingItem) {
        // If the item is already in the cart, update the quantity
        const existingQuantity = parseInt(existingItem.querySelector('.quantity').textContent);
        existingItem.querySelector('.quantity').textContent = existingQuantity + quantity;
    } else {
        // Create a new list item
        const listItem = document.createElement('li');
        listItem.textContent = itemName;

        // Create a quantity span
        const quantitySpan = document.createElement('span');
        quantitySpan.className = 'quantity';
        quantitySpan.textContent = quantity;

        // Set attributes for the list item
        listItem.setAttribute('data-item', itemName);
        listItem.setAttribute('class', 'cart-item');

        // Create a remove button
        const removeButton = document.createElement('button');
        removeButton.textContent = "Remove";
        removeButton.className = "remove-button";
        removeButton.onclick = function() {
            removeItem(itemName);
        };

        // Append quantity span and remove button to the list item
        listItem.appendChild(quantitySpan);
        listItem.appendChild(removeButton);

        // Append the list item to the cart
        cartItems.appendChild(listItem);
    }

    // Send the selected item and quantity to the backend
    sendToDatabase(itemName, quantity);
}

function removeItem(itemName) {
    const cartItems = document.getElementById('cart-items');
    const itemToRemove = document.querySelector(`#cart-items li[data-item='${itemName}']`);

    if (itemToRemove) {
        // Remove the item from the cart
        cartItems.removeChild(itemToRemove);
    }
}

function sendToDatabase(itemName, quantity) {
    fetch('http://localhost:5000/add-to-cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ itemName, quantity }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Item added to database:', data);
    })
    .catch((error) => {
        console.error('Error adding item to database:', error);
    });
}

// You can add the submitCart function if needed, but it's not shown here.
