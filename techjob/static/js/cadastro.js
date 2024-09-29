function toggleFields() {
    console.log("toggleFields called"); 
    const tipoUsuario = document.getElementById('tipo_usuario').value;
    const freelancerFields = document.getElementById('freelancer_fields');
    const empresaFields = document.getElementById('empresa_fields');
    const submitBtn = document.getElementById('submitBtn');


    freelancerFields.classList.add('hidden');
    empresaFields.classList.add('hidden');
    submitBtn.classList.add('hidden');

    if (tipoUsuario === 'freelancer') {
        freelancerFields.classList.remove('hidden');
        submitBtn.classList.remove('hidden');
    } else if (tipoUsuario === 'empresa') {
        empresaFields.classList.remove('hidden');
        submitBtn.classList.remove('hidden');
    }
}
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
