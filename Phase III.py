
import streamlit as st

st.set_page_config(
    page_title="Polynomial Linked List",
    page_icon="🧮",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e0f2fe, #f3e8ff);
}
h1, h2, h3 {
    color: #312e81;
}
.result {
    background: white;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #7c3aed;
    margin: 10px 0;
    color: #1e1b4b;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 Polynomial Operations")
st.caption("Phase II | Polynomial Addition Using Linked Lists")

# Linked List Node
class Node:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power
        self.next = None


# Polynomial Linked List
class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coefficient, power):
        if coefficient == 0:
            return

        current = self.head
        previous = None

        while current and current.power > power:
            previous = current
            current = current.next

        # Same power: combine coefficients
        if current and current.power == power:
            current.coefficient += coefficient

            if current.coefficient == 0:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
            return

        new_node = Node(coefficient, power)
        new_node.next = current

        if previous:
            previous.next = new_node
        else:
            self.head = new_node

    def search(self, power):
        current = self.head

        while current:
            if current.power == power:
                return current.coefficient
            current = current.next

        return None

    def delete(self, power):
        current = self.head
        previous = None

        while current:
            if current.power == power:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True

            previous = current
            current = current.next

        return False

    def terms(self):
        result = []
        current = self.head

        while current:
            result.append((current.coefficient, current.power))
            current = current.next

        return result

    def display(self):
        terms = self.terms()

        if not terms:
            return "0"

        output = ""

        for coefficient, power in terms:
            number = abs(coefficient)

            if power == 0:
                term = str(number)
            elif power == 1:
                term = "" if number == 1 else str(number)
                term += "x"
            else:
                term = "" if number == 1 else str(number)
                term += f"x^{power}"

            if not output:
                output = ("-" if coefficient < 0 else "") + term
            else:
                sign = " - " if coefficient < 0 else " + "
                output += sign + term

        return output


def create_polynomial(terms):
    polynomial = Polynomial()

    for coefficient, power in terms:
        polynomial.insert(coefficient, power)

    return polynomial


def add_polynomials(p1, p2):
    result = Polynomial()

    for coefficient, power in p1.terms():
        result.insert(coefficient, power)

    for coefficient, power in p2.terms():
        result.insert(coefficient, power)

    return result


# Initialize session state
if "p1_terms" not in st.session_state:
    st.session_state.p1_terms = [(5, 2), (3, 1), (2, 0)]

if "p2_terms" not in st.session_state:
    st.session_state.p2_terms = [(4, 2), (2, 1), (7, 0)]

if "message" not in st.session_state:
    st.session_state.message = ""

if "addition_result" not in st.session_state:
    st.session_state.addition_result = ""


# Input section
st.header("✏️ Enter Polynomial Values")

left, right = st.columns(2)

with left:
    st.subheader("Polynomial 1")

    with st.form("p1_form"):
        count1 = st.number_input(
            "Number of terms",
            min_value=1,
            max_value=10,
            value=len(st.session_state.p1_terms),
            key="count1"
        )

        p1_inputs = []

        for i in range(int(count1)):
            old = (
                st.session_state.p1_terms[i]
                if i < len(st.session_state.p1_terms)
                else (1, 0)
            )

            c, p = st.columns(2)

            with c:
                coefficient = st.number_input(
                    f"Coefficient {i + 1}",
                    value=int(old[0]),
                    key=f"p1c_{i}"
                )

            with p:
                power = st.number_input(
                    f"Power {i + 1}",
                    min_value=0,
                    value=int(old[1]),
                    key=f"p1p_{i}"
                )

            p1_inputs.append((int(coefficient), int(power)))

        save1 = st.form_submit_button("Save Polynomial 1")

        if save1:
            st.session_state.p1_terms = p1_inputs
            st.session_state.message = "Polynomial 1 saved successfully!"
            st.rerun()

    p1 = create_polynomial(st.session_state.p1_terms)
    st.markdown(
        f'<div class="result"><b>Current Polynomial 1</b><br>'
        f'{p1.display()}</div>',
        unsafe_allow_html=True
    )

with right:
    st.subheader("Polynomial 2")

    with st.form("p2_form"):
        count2 = st.number_input(
            "Number of terms",
            min_value=1,
            max_value=10,
            value=len(st.session_state.p2_terms),
            key="count2"
        )

        p2_inputs = []

        for i in range(int(count2)):
            old = (
                st.session_state.p2_terms[i]
                if i < len(st.session_state.p2_terms)
                else (1, 0)
            )

            c, p = st.columns(2)

            with c:
                coefficient = st.number_input(
                    f"Coefficient {i + 1}",
                    value=int(old[0]),
                    key=f"p2c_{i}"
                )

            with p:
                power = st.number_input(
                    f"Power {i + 1}",
                    min_value=0,
                    value=int(old[1]),
                    key=f"p2p_{i}"
                )

            p2_inputs.append((int(coefficient), int(power)))

        save2 = st.form_submit_button("Save Polynomial 2")

        if save2:
            st.session_state.p2_terms = p2_inputs
            st.session_state.message = "Polynomial 2 saved successfully!"
            st.rerun()

    p2 = create_polynomial(st.session_state.p2_terms)
    st.markdown(
        f'<div class="result"><b>Current Polynomial 2</b><br>'
        f'{p2.display()}</div>',
        unsafe_allow_html=True
    )

if st.session_state.message:
    st.info(st.session_state.message)


# Addition
st.divider()
st.header("➕ Add Polynomials")

if st.button("Calculate P1 + P2", type="primary"):
    p1 = create_polynomial(st.session_state.p1_terms)
    p2 = create_polynomial(st.session_state.p2_terms)
    result = add_polynomials(p1, p2)
    st.session_state.addition_result = result.display()

if st.session_state.addition_result:
    st.markdown(
        f'<div class="result"><b>Result</b><br>'
        f'{st.session_state.addition_result}</div>',
        unsafe_allow_html=True
    )


# Search, Delete and Insert
st.divider()
st.header("🔧 Polynomial Operations")

selected = st.selectbox(
    "Choose polynomial",
    ["Polynomial 1", "Polynomial 2"]
)

key = "p1_terms" if selected == "Polynomial 1" else "p2_terms"


def get_selected_polynomial():
    return create_polynomial(st.session_state[key])


search_tab, delete_tab, insert_tab = st.tabs(
    ["🔍 Search", "🗑️ Delete", "➕ Insert"]
)

with search_tab:
    search_power = st.number_input(
        "Enter power to search",
        min_value=0,
        step=1,
        key="search_power"
    )

    if st.button("Search Term"):
        polynomial = get_selected_polynomial()
        coefficient = polynomial.search(int(search_power))

        if coefficient is None:
            st.warning(f"No term found with power {search_power}.")
        else:
            st.success(
                f"Term found: coefficient = {coefficient}, "
                f"power = {search_power}"
            )
            st.markdown(
                f'<div class="result">{polynomial.display()}</div>',
                unsafe_allow_html=True
            )

with delete_tab:
    delete_power = st.number_input(
        "Enter power to delete",
        min_value=0,
        step=1,
        key="delete_power"
    )

    if st.button("Delete Term"):
        polynomial = get_selected_polynomial()

        if polynomial.delete(int(delete_power)):
            st.session_state[key] = polynomial.terms()
            st.success("Term deleted successfully!")
            st.markdown(
                f'<div class="result"><b>Updated Polynomial</b><br>'
                f'{polynomial.display()}</div>',
                unsafe_allow_html=True
            )
        else:
            st.warning(f"No term exists with power {delete_power}.")

with insert_tab:
    insert_coefficient = st.number_input(
        "Enter coefficient",
        value=1,
        key="insert_coefficient"
    )

    insert_power = st.number_input(
        "Enter power",
        min_value=0,
        value=0,
        key="insert_power"
    )

    if st.button("Insert Term"):
        polynomial = get_selected_polynomial()
        polynomial.insert(
            int(insert_coefficient),
            int(insert_power)
        )

        st.session_state[key] = polynomial.terms()
        st.success("Term inserted/combined successfully!")
        st.markdown(
            f'<div class="result"><b>Updated Polynomial</b><br>'
            f'{polynomial.display()}</div>',
            unsafe_allow_html=True
        )

st.divider()
st.caption("Polynomial Addition Using Linked Lists | Phase II")
                      
