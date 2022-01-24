<script lang="ts">
  import {
    Collapse,
    Navbar,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
  } from 'sveltestrap';


</script>

<Navbar color="light" light expand="md">
  <NavbarBrand href="/">Globalizzazione</NavbarBrand>
  <Collapse  navbar expand="md">
    <Nav class="ms-auto" navbar>
      <NavItem>
        <NavLink href="/credits">Credits</NavLink>
      </NavItem>

      <NavItem>
        <NavLink href="https://github.com/bestguy/sveltestrap">GitHub</NavLink>
      </NavItem>

    </Nav>
  </Collapse>
</Navbar>