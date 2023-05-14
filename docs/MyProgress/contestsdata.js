var data = {
	labels: ['Weekly Contest - 102', 'Weekly Contest - 103'],
	datasets: [
		{
			label: 'Leetcode',
			fillColor: 'rgba(75, 192, 192, 0.2)',
			strokeColor: 'rgb(75, 192, 192)',
			pointColor: 'rgb(75, 192, 192)',
			pointStrokeColor: '#fff',
			pointHighlightFill: '#fff',
			pointHighlightStroke: 'rgb(75, 192, 192)',
			data: [2, 0],
		},
	],
};

var ctx2 = document.getElementById('myChart2').getContext('2d');
var myBarChart = new Chart(ctx2).Bar(data);
