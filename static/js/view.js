async function loadForm(formId) {
  const res = await fetch(`/forms/${formId}`);
  const form = await res.json();
  const container = document.getElementById('form-container');
  const submitBtn = document.getElementById('submit');
  form.fields.forEach(f => {
    const field = document.createElement('div');
    field.className = 'mb-2';
    field.innerHTML = `<label class='block'>${f.label}</label><input name="${f.name}" type="${f.type}" class="border p-1 w-full" />`;
    container.appendChild(field);
  });

  submitBtn.onclick = async () => {
    const data = {};
    form.fields.forEach(f => {
      data[f.name] = container.querySelector(`[name="${f.name}"]`).value;
    });
    const res = await fetch(`/forms/${formId}/submit`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({data})
    });
    const j = await res.json();
    alert('Submission ID ' + j.id);
  };
}
