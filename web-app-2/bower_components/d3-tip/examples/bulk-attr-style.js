import {
  axisBottom,
  axisLeft,
  max,
  select,
  scaleLinear,
  scaleBand,
  range
} from 'd3';
import d3Tip from '../src/index';

var tip = d3Tip()
  .attr({'class': 'd3-tip', title: 'Some tooltip'})
  .style({border: '1px solid #fff', 'box-shadow': '1px 1px 4px rgba(0,0,0,0.5)', 'border-radius': 'none', 'background-color': 'coral'})
  .html(function(d) { return '<span>' + d.total + '</span>' + ' entries' })
  .offset([-12, 0])

console.log(tip.attr('class'))
var w = 800,
    h = 300,
    padt = 20, padr = 20, padb = 60, padl = 30,
    x  = scaleBand().rangeRound([0, w - padl - padr]).padding(0.1),
    y  = scaleLinear().range([h, 0]),
    yAxis = axisLeft(y).tickSize(-w + padl + padr),
    xAxis = axisBottom(x)

var vis = select('#graph')
  .append('svg')
  .attr('width', w)
  .attr('height', h + padt + padb)
.append('g')
  .attr('transform', 'translate(' + padl + ',' + padt + ')')

var maxValue = max(data, function(d) { return d.total })
x.domain(range(data.length))
y.domain([0, maxValue])

vis.call(tip)
vis.append("g")
  .attr("class", "y axis")
  .call(yAxis)

vis.append("g")
  .attr("class", "x axis")
  .attr('transform', 'translate(0,' + h + ')')
  .call(xAxis)
  .selectAll('.x.axis g')
    .style('display', function (d, i) { return i % 3 != 0  ? 'none' : 'block' })

var bars = vis.selectAll('g.bar')
  .data(data)
.enter().append('g')
  .attr('class', 'bar')
  .attr('transform', function (d, i) { return "translate(" + x(i) + ", 0)" })

bars.append('rect')
  .attr('width', function() { return x.bandwidth() })
  .attr('height', function(d) { return h - y(d.total) })
  .attr('y', function(d) { return y(d.total) })
  .on('mouseover', function(d) {
    tip.show(d)
    console.log(tip.style('box-shadow'))
  })
  .on('mouseout', tip.hide)
