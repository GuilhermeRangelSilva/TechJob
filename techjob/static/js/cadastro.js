function toggleFields() {
    console.log("toggleFields called"); 
    const tipoUsuario = document.getElementById('tipo_usuario').value;
    const freelancerFields = document.getElementById('freelancer_fields');
    const empresaFields = document.getElementById('empresa_fields');
    const submitBtn = document.getElementById('submitBtn');

    // Ocultar todos os campos e o botão de envio
    freelancerFields.classList.add('hidden');
    empresaFields.classList.add('hidden');
    submitBtn.classList.add('hidden');

    // Remover o atributo required de todos os campos
    document.querySelectorAll('#freelancer_fields input, #freelancer_fields select').forEach(field => {
        field.removeAttribute('required');
    });
    document.querySelectorAll('#empresa_fields input, #empresa_fields select').forEach(field => {
        field.removeAttribute('required');
    });

    // Exibir os campos corretos e adicionar required
    if (tipoUsuario === 'freelancer') {
        freelancerFields.classList.remove('hidden');
        submitBtn.classList.remove('hidden');
        document.querySelectorAll('#freelancer_fields input, #freelancer_fields select').forEach(field => {
            field.setAttribute('required', 'required');
        });
    } else if (tipoUsuario === 'empresa') {
        empresaFields.classList.remove('hidden');
        submitBtn.classList.remove('hidden');
        document.querySelectorAll('#empresa_fields input, #empresa_fields select').forEach(field => {
            field.setAttribute('required', 'required');
        });
    }
}

document.getElementById('tipo_usuario').addEventListener('change', toggleFields);

document.getElementById('confirm_password').addEventListener('input', function() {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm_password').value;

    if (password === confirmPassword) {
        document.getElementById('password').classList.remove('input-error');
        document.getElementById('confirm_password').classList.remove('input-error');
        document.getElementById('password').classList.add('input-success');
        document.getElementById('confirm_password').classList.add('input-success');
    } else {
        document.getElementById('password').classList.remove('input-success');
        document.getElementById('confirm_password').classList.remove('input-success');
        document.getElementById('password').classList.add('input-error');
        document.getElementById('confirm_password').classList.add('input-error');
    }
});

document.getElementById('registrationForm').addEventListener('submit', function(event) {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm_password').value;

    if (password !== confirmPassword) {
        event.preventDefault();
        alert('As senhas não coincidem. Por favor, verifique.');
    }
});
