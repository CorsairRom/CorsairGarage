const loadBikes = async (rut) =>{
    try {
        const resp = await fetch(`/get_moto_rut/${rut}`);
        console.log(resp);
        const data = await resp.json();
        if (data.message === 'success') {
            data.moto.forEach(bike => {
                let patente = bike.patente_vh;
                let marca = bike.marca_vh;
                let modelo = bike.modelo_vh;
                let cc = bike.cilindrada_vh;
                console.log(patente);
                let divText = document.getElementById('textQuery');
                let text = document.createElement('h5');
                text.innerHTML = patente + ' ' + marca + ' ' + modelo + ' ' + cc + 'cc';
                divText.append(text);
            });
        }
        else {
            console.log('Motos no encontradas');
        };
    } catch (error) {
        console.log(error);

    }
};

const loadClient = async (rut) => {
    try {
        const response = await fetch(`/get_client/${rut}`);
        console.log(response);
        const data = await response.json();
        if (data.message === 'success') {
            
            data.cliente.forEach(client => {
                let rut_cli = client.rut_cli;
                let title = document.getElementById('exampleModalLabel');
                title.innerHTML = "Cliente Registrado!";
                $('#footerModal').css('display', 'none');
                $('#modalQuery').modal('show');
                loadBikes(rut_cli);
            });
            return true;
        }
        else {
            return false;
            let text = document.getElementById('modalText');
            text.innerHTML = "Cliente No registrado!";
            $('#modalQuery').modal('show');
        };
    } catch (error) {
        console.log(error);

    }
};

const firstLoad = async (rut) => {
    return await loadClient(rut);
};

const captureInputrut = async (event) => {
    event.preventDefault();
    const rut = document.querySelector('#buscarCliente').value;
    await firstLoad(rut);
};




const consulta = async (rut) => {
    console.log(rut);
    try {
        console.log("entro al try");
        const resp = await fetch(`/get_moto_rut/${rut}`);
        const data = await resp.json();
        if (data.message === 'success') {
            
            alert("Encontrado")
        } else {
            
        }
    } catch (error) {
        console.log(error);
    }
};



const captureInput = async (event) => {
    const rut = document.querySelector('#buscarCliente').value;
    try {
        
        const resp = await fetch(`/get_moto_rut/${rut}`);
        const data = await resp.json();
        if (data.message === 'success') {
            window.location.replace(`/view-bikes-client/${rut}`);
            
        } else {
            console.log("usuario no encontrado");
            $('#modalQuery').modal('show');
        };
    } catch (error) {
        console.log(error);
    }
};
