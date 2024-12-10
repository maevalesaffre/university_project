(** Logique+ : CTP1 *)

(** Le début du fichier contient les quelques définitions et lemmes utiles pour
    le contrôle TP. Les lemmes ne sont qu'admis, il ne faut pas les démontrer.

    Les exercices à réaliser pour le contrôle TP se trouvent après le commentaire :
    DEBUT CTP1
 *)


Fixpoint plus (n m:nat) :=
  match n with
  | O => m
  | S n' => S (plus n' m)
  end.

Notation "x + y" := (plus x y)
                       (at level 50, left associativity)
                       : nat_scope.

Fixpoint mult (n m:nat) :=
  match n with
  | O => O
  | S n' => m + mult n' m
end.

Notation "x * y" := (mult x y)
                       (at level 40, left associativity)
                       : nat_scope.

Fixpoint double (n:nat) :=
  match n with
  | O => O
  | S n' => S (S (double n'))
  end.

Theorem plus_0_r : forall n:nat, n + 0 = n.
Proof.
  (* Ne pas démontrer *)
Admitted.

Theorem plus_n_Sm : forall n m : nat,
  S (n + m) = n + (S m).
Proof.
  (* Ne pas démontrer *)
Admitted.
Theorem plus_comm : forall n m : nat,
  n + m = m + n.
Proof.
  (* Ne pas démontrer *)
Admitted.

Theorem plus_assoc : forall n m p : nat,
  n + (m + p) = (n + m) + p.
Proof.
  (* Ne pas démontrer *)
Admitted.

Theorem mult_0_r : forall n:nat,
  n * 0 = 0.
Proof.
  (* Ne pas démontrer *)
Admitted.

Theorem mult_n_Sm: forall n m: nat,
    n * S m = n + n * m.
Proof.
  (* Ne pas démontrer *)
Admitted.

Theorem mult_plus_distr_r : forall n m p : nat,
  (n + m) * p = (n * p) + (m * p).
Proof.
  (* Ne pas démontrer *)
Admitted.

Theorem mult_assoc : forall n m p : nat,
  n * (m * p) = (n * m) * p.
Proof.
  (* Ne pas démontrer *)
Admitted.

Theorem mult_comm : forall m n : nat,
  m * n = n * m.
Proof.
  (* Ne pas démontrer *)
Admitted.

Inductive natlist : Type :=
  | nil
  | cons (n : nat) (l : natlist).

Notation "x :: l" := (cons x l)
                     (at level 60, right associativity).
Notation "[ ]" := nil.
Notation "[ x ; .. ; y ]" := (cons x .. (cons y nil) ..).

Fixpoint length (l:natlist) : nat :=
  match l with
  | nil => O
  | h :: t => S (length t)
  end.

Fixpoint app (l1 l2 : natlist) : natlist :=
  match l1 with
  | nil    => l2
  | h :: t => h :: (app t l2)
  end.

Notation "x ++ y" := (app x y)
                     (right associativity, at level 60).

Fixpoint rev (l:natlist) : natlist :=
  match l with
  | nil    => nil
  | h :: t => rev t ++ [h]
  end.


Theorem nil_app : forall l : natlist,
  [] ++ l = l.
Proof.
    (* Ne pas démontrer *)
Admitted.

Theorem app_nil: forall l : natlist, l ++ [] = l.
Proof.
  (* Ne pas démontrer *)
Admitted.

Theorem app_assoc : forall l1 l2 l3 : natlist,
  (l1 ++ l2) ++ l3 = l1 ++ (l2 ++ l3).
Proof.
    (* Ne pas démontrer *)
Admitted.

(** DEBUT CTP1 *)

(** Exercice 1 : des propriétés sur les entiers.

    Démontrer les lemmes suivants.
 *)

(** Question 1.1 *)

Lemma mult_1_r: forall n, n*1 = n.
Proof.
intro n.
rewrite mult_n_Sm. simpl. rewrite mult_0_r. rewrite plus_0_r. reflexivity.
Qed.
(** Question 1.2 *)

Lemma double_mult2: forall n, double n = n * 2.
Proof.
intro n.
  induction n as [| n' IHn'].
  + simpl. reflexivity.
  + simpl. rewrite IHn'. reflexivity.
Qed.

(** Question 1.3 *)

Lemma double_2mult: forall n, double n = 2 * n.
Proof.
intro n.
simpl. rewrite double_mult2. rewrite -> plus_0_r. rewrite -> mult_n_Sm. rewrite -> mult_1_r. reflexivity.
Qed.


(** Exercice 2 : exponentiation.

Démontrer les lemmes suivants.

NB : faites bien attention à l'argument qui est examiné par la fonction pow pour
    faire avancer le calcul.

 *)
Fixpoint pow (n m: nat) : nat :=
  match m with
  | 0 => 1
  | S m' => n * pow n m'
  end.


(** Question 2.1 *)


Lemma pow_one: forall n,
    pow 1 n = 1.
Proof.
intro n.
  induction n as [| n' IHn'].
  + simpl. reflexivity.
  + simpl. rewrite IHn'. simpl. reflexivity.
Qed.

(** Question 2.2 *)

Lemma pow_plus_mult: forall n m p,
    pow n (m+p) = pow n m * pow n p.
Proof.
intros n m p.
  induction m as [| n' IHn'].
  + simpl. rewrite plus_0_r. reflexivity.
  + simpl. rewrite IHn'. rewrite mult_assoc. reflexivity.
Qed.

(** Question 2.3 *)
(** Ces deux lemmes sont technique. Il n'est pas utile de faire des preuves par
récurrence. Les lois de la multiplication sont suffisantes. Pensez à
démontrer des égalités intermédiaires avec la tactique assert. *)

Lemma mult_com_12 : forall a b c,
    a*(b*c) = b*(a*c).
Proof.
intros a b c.
rewrite mult_assoc. rewrite mult_assoc. 
  assert (H: a * b = b * a).
    { rewrite mult_comm. simpl. reflexivity. }
  rewrite -> H. reflexivity.
Qed.

Lemma mult_distr_com: forall a b c d,
    a*b*(c*d) = a*c*(b*d).
Proof.
Admitted.

(** Question 2.4 *)

Lemma pow_mult_distr: forall n m p,
    pow (n*m) p = pow n p * pow m p.
Proof.
intros n m p.
  induction p as [| n' IHn'].
  + simpl. reflexivity.
  + simpl. rewrite IHn'. rewrite mult_distr_com. rewrite mult_assoc. reflexivity.
Qed.


(** Question 2.5 *)
(** Completer la démonstration ci-dessous *)
Lemma pow_pow_mult: forall n m p,
    pow (pow n m) p = pow n (m * p).
Proof.
  intros n m p.
  induction p as [| p' IHp'].
  + simpl. rewrite mult_0_r. simpl. reflexivity.
  + simpl. rewrite -> IHp'. rewrite mult_comm. rewrite <- pow_plus_mult. rewrite mult_n_Sm. rewrite plus_comm. reflexivity.
Qed.

(** Question 2.6 *)
(** Completer la démonstration ci-dessous *)
(** Il n'est bien entendu pas question d'utiliser le lemme de la question
précédente pour montre ce lemme. *)

Lemma pow_pow_mult': forall n m p,
    pow (pow n m) p = pow n (m * p).
Proof.
  intros n m p.
  induction m as [| m' IHm'].
  + simpl. rewrite pow_one. reflexivity.
  + simpl. rewrite pow_mult_distr. rewrite IHm'. rewrite mult_comm. rewrite <- pow_plus_mult. rewrite plus_comm. reflexivity.
Qed.

(** Exercice 3 : somme des entiers d'une liste.

   Démontrer les lemmes suivants.
 *)

Fixpoint sum (l : natlist) : nat :=
  match l with
  | [] => 0
  | n :: t => n + sum t
  end.

(** Question 3.1 *)
Theorem sum_singleton : forall (n : nat), sum [n] = n.
Proof.
intro n.
simpl. rewrite plus_0_r. reflexivity.
Qed.
(** Question 3.2 *)
Theorem sum_app : forall (l1 l2 : natlist), sum (l1 ++ l2) = sum l1 + sum l2.
Proof.
intros l1 l2.
induction l1 as [| n l1' IHl1'].
+ simpl. reflexivity.
+ simpl. rewrite IHl1'. rewrite plus_assoc. reflexivity.
Qed.

(** Question 3.3 *)
Theorem sum_rev : forall (l : natlist), sum (rev l) = sum l.
Proof.
intro l.
induction l as [| n l' IHl'].
+ simpl. reflexivity.
+ simpl. rewrite sum_app. rewrite IHl'. simpl. rewrite plus_0_r. rewrite plus_comm. reflexivity.
Qed.

(** Question 3.4 *)

Theorem double_plus_distr : forall (n m : nat), double (n + m) = double n + double m.
Proof.
intros n m.
  induction n as [| n' IHn'].
  + simpl. reflexivity.
  + simpl. rewrite IHn'. reflexivity.
Qed.



(** Question 3.5 *)
Fixpoint map (f : nat -> nat) (l : natlist) : natlist :=
  match l with
  | [] => []
  | n :: t => (f n) :: map f t
  end.


Theorem sum_map_double : forall (l : natlist), sum (map double l) = double (sum l).
Proof.
intro l.
induction l as [| n l' IHl'].
+ simpl. reflexivity.
+ simpl. rewrite IHl'. rewrite double_plus_distr. reflexivity.
Qed.

(** Question 3.6 *)

(** Définir une fonction n_fst_nat qui prenant un entier n renvoie la liste [n; n-1; ..., 1]*)

Fixpoint n_fst_nat (n:nat) :=
match n with
  | O => nil
  | S n' => [S n'] ++ n_fst_nat n'
end.

Example ex_n_fst_nat_0 : n_fst_nat 0 = [].
Proof. simpl. reflexivity. Qed.

Example ex_n_fst_nat_1 : n_fst_nat 1 = [1].
Proof. simpl. reflexivity. Qed.

Example ex_n_fst_nat_8 : n_fst_nat 8 = [8; 7; 6; 5; 4; 3; 2; 1].
Proof. simpl. reflexivity. Qed.

(** Question 3.7 *)

(** Ces deux lemmes sont techniques. Il n'est pas utile de faire des preuves par
récurrence. Les lois de l'addition sont suffisantes. Pensez à
démontrer des égalités intermédiaires avec la tactique assert. *)

Lemma plus_com_12: forall a b c,
    a+(b+c) = b+(a+c).
Proof.
intros a b c.
rewrite plus_assoc. rewrite plus_assoc.
  assert (H: a + b = b + a).
  { simpl. rewrite plus_comm. reflexivity. }
  rewrite H. reflexivity. Qed.


Lemma plus_shuffle: forall a b c d, a+b + (c+d) = a+(c+(b+d)).
Proof.
intros a b c d.
rewrite plus_assoc.
  assert (H: c + (b + d) = b + (c + d)).
  { simpl. rewrite plus_com_12. reflexivity. }
  rewrite H. rewrite plus_assoc. rewrite plus_assoc. reflexivity. Qed.


(** Question 3.8 *)

Lemma sum_n_fst_nat: forall n,
    sum(n_fst_nat n) + sum(n_fst_nat n) = n * S n.
Proof.
intro n.
induction n as [| n IHn'].
+ simpl. reflexivity.
+ simpl. rewrite <- plus_n_Sm. rewrite plus_shuffle. rewrite IHn'. rewrite <- mult_n_Sm. reflexivity.
Qed.
