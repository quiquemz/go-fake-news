import {
  randomNormal,
  randomIrwinHall,
  max,
  select,
  scaleLinear,
  scaleBand,
  range
} from 'd3';
import d3Tip from '../src/index';

var NODES = 5000
var RUNS  = 3

var data = [],
  random = randomNormal(5),
  random2 = randomIrwinHall(1)
for(var i = 0; i < NODES; i++) data.push(random(i))

var tip = d3Tip()
  .attr('class', 'd3-tip')
  .html(function(d) { return d.toFixed(2) })
  .direction('nw')
  .offset([0, 3])

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

// Create some artificial nesting
var gs = vis.append('g').append('g')

var circles = gs.selectAll('circle')
  .data(data)
.enter().append('circle')

circles.attr('r', function(d, i) { return random2(i) * 10 })
  .attr('cx', function(d, i) { return x(i) })
  .attr('cy', y)
  .on('mouseover', tip.show)
  .on('mouseout', tip.hide)

var elements = circles.nodes();
var length = elements.length;
var e = new MouseEvent('mouseover');
for(var i = 0; i <= RUNS; i++) {
  var j = 0
  console.time(i)
  for(j; j < length; j++)
    elements[i].dispatchEvent(e)
  console.timeEnd(i)
}
