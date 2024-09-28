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
