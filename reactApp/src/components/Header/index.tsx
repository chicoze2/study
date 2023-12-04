import { Button } from "../Button";
import { HeaderContainer } from "./styles";

export function Header() {

	return(
			<HeaderContainer>

				<div className="hello-text">
					<h3>Olá, Francisco!</h3>
					<span>Você tem <b>03</b> protocolos abertos.</span>

				</div>

				<div className="home-buttons">
					<Button title='Criar Protocolo'></Button>
					<Button title='Painel Administrativo'></Button>
				</div>

			</HeaderContainer>
	)
}
