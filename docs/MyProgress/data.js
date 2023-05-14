var data = {
	labels: [
		'01',
		'02',
		'03',
		'04',
		'05',
		'06',
		'07',
		'08',
		'09',
		10,
		11,
		12,
		13,
		14,
		15,
		16,
		17,
		18,
		19,
		20,
		21,
		22,
		23,
		24,
		25,
		26,
		27,
		28,
		29,
		30,
	],
	datasets: [
		{
			label: 'LeetCode',
			fillColor: 'rgba(255, 99, 132, 0.2)',
			strokeColor: 'rgb(255, 99, 132)',
			pointColor: 'rgb(255, 99, 132)',
			pointStrokeColor: '#fff',
			pointHighlightFill: '#fff',
			pointHighlightStroke: 'rgb(255, 99, 132)',
			data: [5, 5, 5, 5, 2, 1, 7, 4, 5, 3, 4, 5, 0, 0],
		},
		{
			label: 'CodeForces',
			fillColor: 'rgba(153, 102, 255, 0.2)',
			strokeColor: 'rgb(153, 102, 255)',
			pointColor: 'rgb(153, 102, 255)',
			pointStrokeColor: '#fff',
			pointHighlightFill: '#fff',
			pointHighlightStroke: 'rgb(153, 102, 255)',
			data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 3, 2],
		},
	],
};

const labels = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December',
];
// const data2 = {
// 	labels: labels,
// 	datasets: [
// 		{
// 			label: 'My First Dataset',
// 			data: [65, 59, 80, 81, 56, 55, 40],
// 			backgroundColor: [
// 				'rgba(255, 99, 132, 0.2)',
// 				'rgba(255, 159, 64, 0.2)',
// 				'rgba(255, 205, 86, 0.2)',
// 				'rgba(75, 192, 192, 0.2)',
// 				'rgba(54, 162, 235, 0.2)',
// 				'rgba(153, 102, 255, 0.2)',
// 				'rgba(201, 203, 207, 0.2)',
// 			],
// 			borderColor: [
// 				'rgb(255, 99, 132)',
// 				'rgb(255, 159, 64)',
// 				'rgb(255, 205, 86)',
// 				'rgb(75, 192, 192)',
// 				'rgb(54, 162, 235)',
// 				'rgb(153, 102, 255)',
// 				'rgb(201, 203, 207)',
// 			],
// 			borderWidth: 1,
// 		},
// 	],
// };

var data1 = {
	labels: [
		'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December',
	],
	datasets: [
		{
			label: 'Leetcode',
			fillColor: 'rgba(75, 192, 192, 0.2)',
			strokeColor: 'rgb(75, 192, 192)',
			pointColor: 'rgb(75, 192, 192)',
			pointStrokeColor: '#fff',
			pointHighlightFill: '#fff',
			pointHighlightStroke: 'rgb(75, 192, 192)',
			data: [0, 0, 0, 0, 30],
		},
		{
			label: 'Codeforces',
			fillColor: 'rgba(255, 205, 86, 0.2)',
			strokeColor: 'rgb(255, 205, 86)',
			pointColor: 'rgb(255, 205, 86)',
			pointStrokeColor: '#fff',
			pointHighlightFill: '#fff',
			pointHighlightStroke: 'rgb(255, 205, 86)',
			data: [0, 0, 0, 0, 40],
		},
	],
};

var ctx1 = document.getElementById('myChart1').getContext('2d');
var myLineChart = new Chart(ctx1).Line(data);

var ctx2 = document.getElementById('myChart2').getContext('2d');
var myBarChart = new Chart(ctx2).Bar(data1);

var data = {
	labels: [
		'Dynamic Programming',
		'BackTracking',
		'Arrays',
		'Graphs',
		'Trees',
		'LinkedList',
		'Strings',
	],
	datasets: [
		{
			label: 'Leetcode',
			fillColor: 'rgba(54, 162, 235, 0.2)',
			strokeColor: 'rgb(54, 162, 235)',
			pointColor: 'rgb(54, 162, 235)',
			pointStrokeColor: '#fff',
			pointHighlightFill: '#fff',
			pointHighlightStroke: 'rgb(54, 162, 235)',
			data: [117, 28, 248, 134, 116, 47, 155],
		},
		{
			label: 'GeeksForGeeks',
			fill: true,
			fillColor: 'rgba(255, 99, 132, 0.2)',
			strokeColor: 'rgb(255, 99, 132)',
			pointColor: 'rgb(255, 99, 132)',
			pointStrokeColor: '#fff',
			pointHighlight: '#fff',
			pointHighlightStroke: 'rgb(255, 99, 132)',
			data: [51, 9, 118, 42, 120, 67, 42],
		},
	],
};

var ctx3 = document.getElementById('myChart3').getContext('2d');
var myRadarChart = new Chart(ctx3).Radar(data);

var data = [
	{
		value: 668,
		color: '#F7464A',
		highlight: '#FF5A5E',
		label: 'GFG',
	},
	{
		value: 703,
		color: '#46BFBD',
		highlight: '#5AD3D1',
		label: 'Leetcode',
	},
	{
		value: 40,
		color: '#FDB45C',
		highlight: '#FFC870',
		label: 'Codeforces',
	},
	// {
	// 	value: 40,
	// 	color: '#949FB1',
	// 	highlight: '#A8B3C5',
	// 	label: 'Codeforces',
	// },
	// {
	// 	value: 703,
	// 	color: '#4D5360',
	// 	highlight: '#616774',
	// 	label: 'LeetCode',
	// },
];

var ctx4 = document.getElementById('myChart4').getContext('2d');
new Chart(ctx4).PolarArea(data);

var data = [
	{
		value: 65,
		color: '#F7464A',
		highlight: '#FF5A5E',
		label: 'Hard',
	},
	{
		value: 210,
		color: '#46BFBD',
		highlight: '#5AD3D1',
		label: 'Easy',
	},
	{
		value: 428,
		color: '#FDB45C',
		highlight: '#FFC870',
		label: 'Medium',
	},
];

var ctx5 = document.getElementById('myChart5').getContext('2d');
var myPieChart = new Chart(ctx5).Pie(data);

var ctx6 = document.getElementById('myChart6').getContext('2d');
var myDoughnutChart = new Chart(ctx6).Doughnut(data);
