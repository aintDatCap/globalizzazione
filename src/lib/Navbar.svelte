<script lang="ts">
	import { Collapse, Navbar, NavbarBrand, Nav, NavItem, NavLink, Icon } from 'sveltestrap';
	import Sidebar from '$lib/Sidebar.svelte';
	let toggle_sidebar = false;
</script>

<Navbar color="light" light expand="md">
	<div id="list" on:click={() => toggle_sidebar=!toggle_sidebar}>
		<Icon name="list" />
	</div>
	
	<NavbarBrand href="/">Globalizzazione</NavbarBrand>
	<Collapse navbar expand="md">
		<Nav class="ms-auto" navbar>
			<NavItem>
				<NavLink href="/credits">Credits</NavLink>
			</NavItem>

			<NavItem>
				<NavLink href="https://github.com/yrenum/globalizzazione">
					GitHub
					<Icon name="github" />
				</NavLink>

			</NavItem>

		</Nav>
	</Collapse>
</Navbar>
{#if toggle_sidebar}
	<Sidebar />
{/if}

<style>
	#list {
		margin-right: 1em;
		cursor:pointer;
	}
</style>