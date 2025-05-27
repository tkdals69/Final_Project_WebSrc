// 간단한 로딩 오버레이 제어 예시
document.addEventListener('DOMContentLoaded', () => {
  const loader = document.getElementById('loader');
  const forms = document.querySelectorAll('form');

  forms.forEach(form => {
    form.addEventListener('submit', () => {
      loader.classList.remove('hidden');
    });
  });
});
