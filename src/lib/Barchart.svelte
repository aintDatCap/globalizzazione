<script lang="ts">
	import { onMount } from 'svelte';
	import * as d3 from 'd3';

  export let height:number;
  export let width:number;
  export let xRange: number[];
	export let yRange: number[];
  export let minX: number = 0;
	export let minY: number = 0;
  export let xText: string = '';
	export let yText: string = '';
  export let data;
  let chart;

  onMount(()=> {
    const svg = d3.select(chart)
    const xscale = d3
			.scaleLinear()
			.domain([minX, d3.max(xRange)])
			.range([0, width - 100]);

		const yscale = d3
			.scaleLinear()
			.domain([minY, d3.max(yRange)])
			.range([height / 2, 0]);

    const x_axis = d3.axisBottom().scale(xscale);
		const y_axis = d3.axisLeft().scale(yscale);

		svg.append('g').attr('transform', 'translate(50, 10)').call(y_axis);

		const xAxisTranslate = height / 2 + 10;
		svg
			.append('g')
			.attr('transform', 'translate(50, ' + xAxisTranslate + ')')
			.call(x_axis);


    svg.selectAll()
    .data(data)
    .enter()
    .append('rect')
    .attr('x', (d) => xscale(d.x))
    .attr('y', (d) => yscale(d.y))
    .attr('height', (d) => height - yscale(d.value))
    .attr('width', xscale.bandwidth())

    svg
			.append('text')
			.attr('transform', 'rotate(-90)')
			.attr('y', 0)
			.attr('x', -height / 4)
			.attr('dy', '1em')
			.style('text-anchor', 'middle')
			.text(yText);

		svg
			.append('text')
			.attr('x', width/2)
			.attr('y',  height/2+45)
			.style('text-anchor', 'middle')
			.text(xText);
  })


</script>




<svg {height} {width} bind:this={chart} />