async function getJSON() {
  const jsonPromise = await fetch("/api/?");
  return await jsonPromise.json();
}

const json = await getJSON();
const initialData = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0 };
console.log(json);
const DATA = json.users.reduce((previousValue, user) => {
  previousValue[user.generation]++;
  return previousValue;
}, initialData);
console.log(Object.values(DATA));
const DATA_COUNT = 5;
const NUMBER_CFG = { count: DATA_COUNT, min: 0, max: 100 };

const data = {
  labels: ["1기", "2기", "3기", "4기", "5기", "6기", "7기"],
  datasets: [
    {
      label: "Dataset 1",
      data: Object.values(DATA),
      backgroundColor: Object.values({
        red: "rgb(255, 99, 132)",
        orange: "rgb(255, 159, 64)",
        yellow: "rgb(255, 205, 86)",
        green: "rgb(75, 192, 192)",
        blue: "rgb(54, 162, 235)",
        purple: "rgb(153, 102, 255)",
        grey: "rgb(201, 203, 207)",
      }),
    },
  ],
};
const config = {
  type: "pie",
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "동신과학고 졸업생 계열표",
      },
    },
  },
};
const myChart = new Chart(document.getElementById("myChart"), config);
