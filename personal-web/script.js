// Dark mode toggle and persistence
(function() {
    const toggleBtn = document.createElement('button');
    toggleBtn.id = 'dark-mode-toggle';
    toggleBtn.innerText = '🌙 Dark Mode';
    toggleBtn.style.position = 'fixed';
    toggleBtn.style.top = '1em';
    toggleBtn.style.right = '1em';
    toggleBtn.style.zIndex = '999';
    toggleBtn.style.padding = '0.5em 1em';
    toggleBtn.style.borderRadius = '6px';
    toggleBtn.style.border = 'none';
    toggleBtn.style.background = '#222';
    toggleBtn.style.color = '#fff';
    toggleBtn.style.cursor = 'pointer';
    toggleBtn.style.fontSize = '1em';
    document.body.appendChild(toggleBtn);

    function setDarkMode(on) {
        if (on) {
            document.body.classList.add('dark-mode');
            toggleBtn.innerText = '☀️ Light Mode';
            localStorage.setItem('darkMode', 'on');
        } else {
            document.body.classList.remove('dark-mode');
            toggleBtn.innerText = '🌙 Dark Mode';
            localStorage.setItem('darkMode', 'off');
        }
    }

    toggleBtn.onclick = function() {
        setDarkMode(!document.body.classList.contains('dark-mode'));
    };

    // On load, check localStorage
    if (localStorage.getItem('darkMode') === 'on') {
        setDarkMode(true);
    }
})();
