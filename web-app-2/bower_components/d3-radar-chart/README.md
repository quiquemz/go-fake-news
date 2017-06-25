[![Published on webcomponents.org](https://img.shields.io/badge/webcomponents.org-published-blue.svg)](https://www.webcomponents.org/element/polymerEl/d3-radar-chart)

# d3-radar-chart

Simple element to display a radar-chart

<!--
```
<custom-element-demo>
  <template>
    <link rel="import" href="d3-radar-chart.html">
    <next-code-block></next-code-block>
  </template>
</custom-element-demo>
```
-->
```html
 <d3-radar-chart 
        options='{"maxValue": 20}'
        data='[{"className": "france","circles": true,"axes": [{"axis": "strength","value": 19}, {"axis": "intelligence","value": 8}, {"axis": "charisma","value": 15}, {"axis": "dexterity","value": 15}, {"axis": "luck","value": 12}]  }, {"className": "germany", "axes": [{"axis": "strength","value": 13}, {"axis": "intelligence","xOffset": -20,"value": 6}, {"axis": "charisma","value": 5}, {"axis": "dexterity","value": 9}, {"axis": "luck","value": 2}]}]'
      ></d3-radar-chart>
```