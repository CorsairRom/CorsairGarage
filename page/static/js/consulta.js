

const loadMbikes = async (patente) => {
    console.log(patente);
    try {
        const response = await fetch(`/get_moto/${patente}`);
        console.log(response);
        const data = await response.json();
        console.log(data);
        if (data.message === 'success') {
            let count = 0;
            data.Mbike.forEach(bike => {
                count = count + 1;
                tabla = document.getElementById("tableData");
                let tr = document.createElement("tr");
                let col1 = document.createElement("td");
                col1.innerHTML = count;
                let col2 = document.createElement("td");
                col2.innerHTML = bike.patente_vh;
                let col3 = document.createElement("td");
                col3.innerHTML = bike.marca_vh;
                let col4 = document.createElement("td");
                col4.innerHTML = bike.modelo_vh;
                let col5 = document.createElement("td");
                col5.innerHTML = bike.cilindrada_vh;
                tabla.appendChild(tr);
                tr.appendChild(col1)
                tr.appendChild(col2)
                tr.appendChild(col3)
                tr.appendChild(col4)
                tr.appendChild(col5)
            });
        };
        
    } catch (error) {
        console.log(error);
    }
};


const firstLoad = async (patente) => {
    await loadMbikes(patente);
};

// window.addEventListener('load', async () => {
//     const patente = 'EH-311'
//     await firstLoad(patente);
// });

const captureInputPatente = async (event) => {
    event.preventDefault();
    const patente = document.querySelector('#buscarPatente').value;
    // document.querySelector('#btnConsultarPatente').disabled = true;
    await firstLoad(patente);
    console.log(patente);
};