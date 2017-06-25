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
  .attr('class', 'd3-tip')
  .html(function(d) { return '<span>' + d.total + '</span>' + ' entries' })
  .offset([-12, 0])

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
    tip.attr('class', 'd3-tip animate').show(d)
  })
  .on('mouseout', function(d) {
    tip.attr('class', 'd3-tip').show(d)
    tip.hide()
  })
