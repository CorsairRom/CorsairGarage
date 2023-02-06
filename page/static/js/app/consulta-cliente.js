const loadClient = async (rut) => {
    try {
        const response = await fetch(`/get_client/${rut}`);
        console.log(response);
        const data = await response.json();
        if (data.message === 'success') {
            data.cliente.forEach(client => {
                let rut_cli = client.rut_cli;
                let text = document.getElementById('modalText');
                text.innerHTML = "Cliente Registrado!";
                $('#footerModal').css('display', 'none');
                $('#modalQuery').modal('show');
            });
        }
        else {
            let text = document.getElementById('modalText');
            text.innerHTML = "Cliente No registrado!";
            $('#modalQuery').modal('show');
        };
    } catch (error) {
        console.log(error);

    }
};

const firstLoad = async (rut) => {
    await loadClient(rut);
};

const captureInputrut = async (event) => {
    event.preventDefault();
    const rut = document.querySelector('#buscarCliente').value;
    await firstLoad(rut);
};