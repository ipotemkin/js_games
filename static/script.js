
function launchGameOne() {
    let season = "";
    let month = 0;
    while (true) {
        month = prompt("Введите номер месяца (от 1 до 12)");
        
        // проверяем, что пользователь нажал на кнопку "отмена"
        if (month === null) {
            return;
        }
        
        month = parseInt(month);  // переводим в int
        
        if (month >= 1 && month <= 12) {
            break;
        } else {
            alert("Неверный номер месяца");
        }
    }

    if (month >= 3 && month <=5) {
        season = "весна";
    } else if (month >= 6 && month <=8) {
        season = "лето";
    } else if (month >= 9 && month <= 11) {
        season = "осень";
    } else {
        season = "зима";
    }
    msg = `Вы ввели месяц ${month}, это ${season}`;        
    console.log(msg);  // выводим в консоль
    alert(msg);  // выводим на экран
}


let months = {
    1: ["январь", 1],
    2: ["февраль", 1],
    3: ["март", 2],
    4: ["апрель", 2],
    5: ["май", 2],
    6: ["июнь", 3],
    7: ["июль", 3],
    8: ["август", 3],
    9: ["сентябрь", 4],
    10: ["октябрь", 4],
    11: ["ноябрь", 4],
    12: ["декабрь", 1]
};

let seasons = {
    1: "зима",
    2: "весна",
    3: "лето",
    4: "осень"
};

function launchGameOne_2() {    
    let month = "";
    while (true) {
        month = prompt("Введите номер месяца (от 1 до 12)");
        
        // проверяем, что пользователь нажал на кнопку "отмена"
        if (month === null) {
            return;
        }
        
        month = month.trim()  // убираем начальные и конечные пробелы
        if (month in months) {
            break;
        } else {
            alert("Неверный номер месяца");
        }        
    }

    let month_name = months[month][0];
    let season_name= seasons[months[month][1]];
    msg = `Вы ввели месяц ${month} (${month_name}), это ${season_name}`;        
    console.log(msg);  // выводим в консоль
    alert(msg);  // выводим на экран
}
