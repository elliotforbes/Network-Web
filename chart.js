var chart = c3.generate({
    bindto: '#networkStats',
    data: {
        columns: [
            ['SSDP', 30],
            ['BitTorrent', 120],
            ['DHCPV6', 70],
            ['NetBIOS', 160],
            ['Other', 50],
        ],
        type : 'donut',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    },
    donut: {
        title: "Top Application Protocols"
    }
});

var chart2 = c3.generate({
    bindto: '#throughput',
    data: {
      columns: [
        ['ThroughPut - Pi 1', 200, 195, 205, 185, 200, 300],
        ['ThroughPut - Pi 2', 190, 200, 195, 205, 185, 200]
      ],
      axes: {
        data2: 'y2' // ADD
      }
    },
    axis: {
      y2: {
        show: false // ADD
      }
    }
});

var chart3 = c3.generate({
    bindto: '#chart3',
    data: {
        columns: [
            ['data1', 300, 350, 300, 0, 0, 0],
            ['data2', 130, 100, 140, 200, 150, 50]
        ],
        types: {
            data1: 'area',
            data2: 'area-spline'
        }
    }
});

var chart4 = c3.generate({
    bindto: '#chart4',
    data: {
        columns: [
            ['Upload', 300, 350, 420, 500, 527, 619],
            ['Download', 10, 18, 23, 25, 31, 37]
        ],
        types: {
            data1: 'area',
            data2: 'area-spline'
        }
    }
});