<script lang="ts">
  import {onMount} from "svelte";
  import * as d3 from "d3";

  export let data:number[];
  export let height:number;
  export let width:number;
  export let colors:string[];
  export let innerRadius:number;

  let chart;

  onMount(() => {
    const svg = d3.select(chart);
    const radius = Math.min(width, height) / 2;
    const g = svg.append("g").attr("transform", `translate( ${width/2} , ${height/2} )`);

    const pie = d3.pie();
    const arc = d3.arc().innerRadius(innerRadius).outerRadius(radius);
  

    
    const arcs = g.selectAll("arc")
      .data(pie(data))
      .enter()
      .append("g")
      .attr("class", "arc") 

    arcs.append("path")
      .attr("fill", (d,i) => {
        return colors[i];
      })
      .attr("d", arc);
  })
</script>

<svg height={height} width={width} bind:this={chart}/>