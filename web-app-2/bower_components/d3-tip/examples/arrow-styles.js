import {
  randomNormal,
  randomIrwinHall,
  max,
  select,
  scaleLinear
} from 'd3';
import d3Tip from '../src/index';

var data = [],
  random = randomNormal(5),
  random2 = randomIrwinHall(1)
for(var i = 0; i < 25; i++) data.push(random(i))

var w = 200,
    h = 200,
    b = 20,
    r = 10,
    x = scaleLinear().domain([0, data.length - 1]).range([r, w - r]),
    y = scaleLinear().domain([0, max(data)]).range([h,  0])

var directions = ['n', 'w', 'e', 's'];
directions.forEach(function (direction) {
  var tip = d3Tip()
    .attr('class', 'd3-tip')
    .html(function(d) { return d.toFixed(2) })
    .direction(direction)
    .offset(function () {
      if(direction=='n') { return [-10,0] }
      else if(direction=='s') { return [10,0] }
      else if(direction=='e') { return [0,10] }
      else if(direction=='w') { return [0,-10] }
    })

  var vis = select(document.body)
    .append('svg')
    .attr('class', direction)
    .attr('width', w)
    .attr('height', h)
  .append('g')
    .attr('transform', 'translate('+b+','+b+')')
  .call(tip)

  vis.append('text')
    .attr('class', 'direction')
    .attr('x', w/2)
    .attr('y', -b)
    .attr('dy', '1em')
    .text('direction: ' + direction)

  vis.selectAll('circle')
    .data(data)
  .enter().append('circle')
    .attr('r', function(d, i) { return random2(i) * 10 })
    .attr('cx', function(d, i) { return x(i) })
    .attr('cy', y)
    .on('mouseover', tip.show)
    .on('mouseout', tip.hide)
})
