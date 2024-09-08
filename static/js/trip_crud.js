document.addEventListener('DOMContentLoaded', function () {
    fetchTrips(); // Fetch trips on page load

    // Handle form submission for adding a new trip
    document.getElementById('addTripForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const name = document.getElementById('tripName').value;
        const location = document.getElementById('tripLocation').value;
        const price = document.getElementById('tripPrice').value;

        // Call the POST API to create a new trip
        fetch('/api/trips', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, location, price }),
        })
        .then(response => response.json())
        .then(data => {
            alert('Trip added successfully!');
            $('#addTripModal').modal('hide');
            fetchTrips(); // Refresh the trips table
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

// Fetch all trips and display in table
function fetchTrips() {
    fetch('/api/trips')
        .then(response => response.json())
        .then(trips => {
            const tableBody = document.getElementById('tripTableBody');
            tableBody.innerHTML = ''; // Clear existing rows

            trips.forEach(trip => {
                const row = `
                    <tr>
                        <td>${trip.id}</td>
                        <td>${trip.name}</td>
                        <td>${trip.location}</td>
                        <td>${trip.price}</td>
                        <td>
                            <button class="btn btn-info btn-sm" onclick="viewTrip(${trip.id})">View</button>
                            <button class="btn btn-danger btn-sm" onclick="deleteTrip(${trip.id})">Delete</button>
                        </td>
                    </tr>`;
                tableBody.insertAdjacentHTML('beforeend', row);
            });
        });
}

// View a specific trip
function viewTrip(id) {
    fetch(`/api/trips/${id}`)
        .then(response => response.json())
        .then(trip => {
            alert(`Trip Details:\nName: ${trip.name}\nLocation: ${trip.location}\nPrice: ${trip.price}`);
        })
        .catch(error => {
            alert('Trip not found.');
            console.error('Error:', error);
        });
}

// Delete a specific trip
function deleteTrip(id) {
    if (confirm('Are you sure you want to delete this trip?')) {
        fetch(`/api/trips/${id}`, {
            method: 'DELETE',
        })
        .then(() => {
            alert('Trip deleted successfully!');
            fetchTrips(); // Refresh the trips table
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}
