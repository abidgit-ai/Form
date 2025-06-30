const fieldsContainer = document.getElementById('fields');
const addFieldBtn = document.getElementById('add-field');
const saveFormBtn = document.getElementById('save-form');

function createFieldRow() {
  const row = document.createElement('div');
  row.className = 'flex space-x-2 mb-2';
  row.innerHTML = `
    <input type="text" placeholder="Label" class="border p-1 label" />
    <select class="border p-1 type">
      <option value="text">Text</option>
      <option value="number">Number</option>
    </select>
    <button class="remove bg-red-500 text-white px-2">X</button>
  `;
  row.querySelector('.remove').onclick = () => row.remove();
  return row;
}

addFieldBtn.onclick = () => {
  fieldsContainer.appendChild(createFieldRow());
};

saveFormBtn.onclick = async () => {
  const name = document.getElementById('form-name').value;
  const fields = Array.from(fieldsContainer.children).map((row, index) => {
    return {
      name: `field_${index}`,
      label: row.querySelector('.label').value,
      type: row.querySelector('.type').value
    };
  });

  const res = await fetch('/forms', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({name, fields})
  });
  const data = await res.json();
  alert('Form saved with ID ' + data.id);
};
