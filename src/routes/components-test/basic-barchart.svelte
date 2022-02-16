<script lang="ts">
  import Barchart from "$lib/barchart.svelte"
  import data from "$lib/data/glob_data.json"
  const glob_data = JSON.parse(JSON.stringify(data))

  let xRange: number[] = [];
  let yRange: number[] =[];

  for(let i = 1870; i <= 2000; i+=20) xRange.push(i);
  for(let i = 0; i <= 40; i+=10) yRange.push(i);



</script>

<Barchart 

  {xRange}
  {yRange}
  height={500}
  width={600}
  data={glob_data}
/>