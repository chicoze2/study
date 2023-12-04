import styled from "styled-components"

export const HeaderContainer = styled.section`
	max-width: 80%;

	display: flex;
	margin: auto;
	align-items: center;
	justify-content: space-between;
	padding: 10px;




	.hello-text{

	}

	.home-buttons{
		margin: 8px;
		display: flex;
		flex-direction: column;

		button{

			& + button{
				margin-top: 4px;
			}
		}
	}

`
