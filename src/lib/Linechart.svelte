<script lang="ts">
	import { onMount } from 'svelte';
	import * as d3 from 'd3';
	export let data: number[];
	export let xRange: number[];
	export let yRange: number[];
	export let height: number;
	export let width: number;
	export let minX: number = 0;
	export let minY: number = 0;

	let chart;

	onMount(() => {
		const svg = d3.select(chart);

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
		
	});
</script>

<svg {height} {width} bind:this={chart} />
