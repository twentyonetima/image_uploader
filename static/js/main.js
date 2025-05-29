function getCSRFToken() {
  return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

async function loadImages() {
  try {
    const response = await fetch('/api/list/');
    if (!response.ok) {
      throw new Error(`Ошибка при загрузке списка изображений: ${response.status}`);
    }
    const data = await response.json();
    const tbody = document.getElementById('image-list');
    tbody.innerHTML = '';
    data.forEach(item => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td style="padding: 8px; vertical-align: middle;">${item.number ?? '—'}</td>
        <td style="padding: 8px; vertical-align: middle;">
          <img src="${item.image}" width="100" style="border: 1px solid #ccc; border-radius: 4px;">
        </td>
        <td style="padding: 8px; vertical-align: middle;">${item.created_at_formatted || item.created_at}</td>
      `;
      tbody.appendChild(tr);
    });
  } catch (error) {
    document.getElementById('error-message').textContent = error.message;
  }
}

document.addEventListener('DOMContentLoaded', function () {
  const uploadForm = document.getElementById('upload-form');
  const massUploadForm = document.getElementById('mass-upload-form');
  const uploadLoader = document.getElementById('upload-loader');
  const massUploadLoader = document.getElementById('mass-upload-loader');

  uploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(uploadForm);
    uploadLoader.style.display = 'block';
    try {
      const response = await fetch('/api/upload/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCSRFToken()
        },
        body: formData
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData?.error || 'Ошибка при загрузке файла');
      }

      await loadImages();
      uploadForm.reset();
    } catch (error) {
      alert(error.message);
    } finally {
      uploadLoader.style.display = 'none';
    }
  });

  massUploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(massUploadForm);
    massUploadLoader.style.display = 'block';
    try {
      const response = await fetch('/api/mass-upload/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCSRFToken()
        },
        body: formData
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData?.error || 'Ошибка при массовой загрузке');
      }

      await loadImages();
      massUploadForm.reset();
    } catch (error) {
      alert(error.message);
    } finally {
      massUploadLoader.style.display = 'none';
    }
  });

  loadImages();
});
