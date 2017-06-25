import {
  axisBottom,
  axisLeft,
  randomNormal,
  randomIrwinHall,
  max,
  select,
  scaleLinear,
  scaleBand,
  range
} from 'd3';
import d3Tip from '../src/index';

var data = [],
  random = randomNormal(5),
  random2 = randomIrwinHall(1)
for(var i = 0; i < 100; i++) data.push(random(i))

var tip = d3Tip()
  .attr('class', 'd3-tip')
  .html(function(d) { return d.toFixed(2) })
  .direction('nw')
  .offset([0, 3])

var tip2 = d3Tip()
  .attr('class', 'd3-tip')
  .html(function(d) { return d.toFixed(2) })
  .direction('n')
  .offset([-3, 0])

var w = 1000,
    h = 500,
    r = 10,
    linex, liney,
    x = scaleLinear().domain([0, data.length - 1]).range([r, w - r]),
    y = scaleLinear().domain([0, max(data)]).range([h,  0])

var vis = select(document.body)
  .append('svg')
  .attr('width', w)
  .attr('height', h)
.append('g')
  .attr('transform', 'translate(20, 20)')
.call(tip)

vis.selectAll('circle')
  .data(data)
.enter().append('circle')
  .attr('r', function(d, i) { return random2(i) * 10 })
  .attr('cx', function(d, i) { return x(i) })
  .attr('cy', y)
  .on('mouseover', tip.show)
  .on('mouseout', tip.hide)

var vis2 = select(document.body)
  .append('svg')
  .attr('width', w)
  .attr('height', h)
.append('g')
  .attr('transform', 'translate(20, 20)')
  .call(tip2)

vis2.selectAll('circle')
  .data(data)
.enter().append('circle')
  .attr('class', 'clickable')
  .attr('r', function(d, i) { return random2(i) * 10 })
  .attr('cx', function(d, i) { return x(i) })
  .attr('cy', y)
  .on('click', function(d) {
    tip2.hide(d).show(d)
  })
