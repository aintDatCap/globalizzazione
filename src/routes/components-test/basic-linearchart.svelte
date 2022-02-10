<script lang="ts">
	import Linechart from '$lib/Linechart.svelte';
	import data from "$lib/data/glob_data.json"

	let xRange: number[] = [];
	let yRange: number[] = [];
	for (let i = 1900; i <= 2015; i++) xRange.push(i);
	for (let i = 0; i <= 110; i += 10) yRange.push(i);

	const glob_data = JSON.parse(JSON.stringify(data))

</script>

<Linechart
	{xRange}
	{yRange}
	data={glob_data}
	height={300}
	width={600}
	minX={1887} />
