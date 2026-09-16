const form = document.getElementById("priceForm");
const result = document.getElementById("result");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const data = {
        location: document.getElementById("location").value,
        area: Number(document.getElementById("area").value),
        bedrooms: Number(document.getElementById("bedrooms").value),
        bathrooms: Number(document.getElementById("bathrooms").value),
        parking: Number(document.getElementById("parking").value),
        property_age: Number(
            document.getElementById("property_age").value
        )
    };

    result.innerHTML = "Calculating...";

    try {
        const response = await fetch("/api/calculate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const responseData = await response.json();

        if (!response.ok) {
            throw new Error(responseData.error || "Calculation failed");
        }

        result.innerHTML =
            "Estimated Price: ₹ " +
            Number(responseData.estimated_price).toLocaleString("en-IN");

    } catch (error) {
        result.innerHTML = "Error: " + error.message;
    }
});
