import { Container } from "./styles";

import logo from "../../assets/logo.svg";
import profile from "../../assets/profile.svg";

export function NavBar() {
	return (
		<Container>
			<div>
				<img src={logo} alt="Logo" />
				<h2>Gerencia de Protocolos</h2>
			</div>

			<div>
				<small>Francisco José</small>
				<img src={profile} alt="Profile icon" />
			</div>
		</Container>
	);
}
