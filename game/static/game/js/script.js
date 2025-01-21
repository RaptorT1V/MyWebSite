let sortDirection = 1;

document.addEventListener('DOMContentLoaded', function () {
    const table = document.querySelector('.leaderboard table');
    const headers = table.querySelectorAll('th');

    setTimeout(() => {
        headers.forEach(header => {
            header.addEventListener('click', () => {
                console.log('Клик на колонку:', header.textContent);
                const columnIndex = Array.from(headers).indexOf(header);
                sortTable(table, columnIndex);
            });
        });
    }, 100);

    function sortTable(table, columnIndex) {
        const tbody = table.querySelector('tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));
        const isNumeric = columnIndex > 0; // Сортируем числа для столбцов 1, 2, 3 (имена не сортируем)

        rows.sort((rowA, rowB) => {
            let valueA = rowA.querySelectorAll('td')[columnIndex].textContent.trim();
            let valueB = rowB.querySelectorAll('td')[columnIndex].textContent.trim();

            if (isNumeric) {
                // Проверяем, является ли valueA или valueB дефисом
                const isValueADash = valueA === "-";
                const isValueBDash = valueB === "-";

                if (isValueADash && isValueBDash) {
                    return 0;
                } else if (isValueADash) {
                    return 1; // Пустые строки в конец
                } else if (isValueBDash) {
                    return -1;
                }

                valueA = parseInt(valueA, 10);
                valueB = parseInt(valueB, 10);

                return (valueB - valueA) * sortDirection;
            }
            else {
                return valueA.localeCompare(valueB) * sortDirection;
            }
        });

        sortDirection *= -1;

        // Обновляем таблицу
        tbody.innerHTML = '';
        rows.forEach(row => tbody.appendChild(row));
    }
});