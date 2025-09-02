document.addEventListener('DOMContentLoaded', function() {
    const appointments = [
        {
            name: "Alan Blessing",
            appointmentTime: "April 15, 2024, 10:00 AM",
            bookedTime: "April 1, 2024, 09:45 AM",
            revenue: 120
        },
        {
            name: "Vidhanshu Kachhwaha",
            appointmentTime: "April 16, 2024, 2:00 PM",
            bookedTime: "April 2, 2024, 10:00 AM",
            revenue: 150
        },
        {
            name: "Anhad Singh",
            appointmentTime: "April 17, 2024, 1:00 PM",
            bookedTime: "April 3, 2024, 11:30 AM",
            revenue: 180
        },
        {
            name: "Shraavya",
            appointmentTime: "April 18, 2024, 11:00 AM",
            bookedTime: "April 4, 2024, 12:45 PM",
            revenue: 200
        }
    ];

    let totalRevenue = 0;
    const appointmentsContainer = document.getElementById('appointments-container');

    appointments.forEach(appointment => {
        totalRevenue += appointment.revenue;
        const appointmentDiv = document.createElement('div');
        appointmentDiv.className = 'card';
        appointmentDiv.innerHTML = `
            <h2>${appointment.name}</h2>
            <p><strong>Appointment:</strong> ${appointment.appointmentTime}</p>
            <p><strong>Booked:</strong> ${appointment.bookedTime}</p>
            <p><strong>Revenue:</strong> ₹${appointment.revenue.toFixed(2)}</p>
        `;
        appointmentsContainer.appendChild(appointmentDiv);
    });

    const totalRevenueDisplay = document.getElementById('revenue');
    totalRevenueDisplay.textContent = `₹${totalRevenue.toFixed(2)}`;
});