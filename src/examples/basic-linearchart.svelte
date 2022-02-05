<script lang="ts">
	import Linechart from '$lib/Linechart.svelte';
	let xRange: number[] = [];
	let yRange: number[] = [];
	for (let i = 1900; i < 2015; i++) xRange.push(i);
	for (let i = 0; i < 100; i += 10) yRange.push(i);
</script>

<Linechart
	{xRange}
	{yRange}
	data={[3.42, 3.9, 4.4, 4.97, 5.54, 6.11, 6.68, 7.25, 7.81, 8.53, 9.25, 14.62, 18.66, 23.87, 28.85, 34.73, 39.82, 47.04, 52.58, 63.1, 76.09, 91.33, 108.12]}
	height={200}
	width={500}
	minX={1900} />
