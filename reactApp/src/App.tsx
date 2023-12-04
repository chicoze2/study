import { GlobalStyles } from "./styles/GlobalStyles"

import { Body } from "./components/Body/styles"
import { NavBar } from "./components/NavBar"
import { Header } from "./components/Header"
import { ProtocolsBoard } from "./components/ProtocolsBoard"

function App() {

  return (
    <Body>
			//Create component to envolve all childres and center
			<GlobalStyles/>
			<NavBar/>
			<Header/>
			<ProtocolsBoard/>
    </Body>
  )
}

export default App
