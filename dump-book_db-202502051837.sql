PGDMP  0    %                }            book_db    17.0 (Debian 17.0-1.pgdg120+1)    17.2 (    K           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            L           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            M           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            N           1262    16384    book_db    DATABASE     r   CREATE DATABASE book_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE book_db;
                     postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                     pg_database_owner    false            O           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                        pg_database_owner    false    4            �            1259    16435    address    TABLE     �   CREATE TABLE public.address (
    id integer NOT NULL,
    street character varying(255) NOT NULL,
    city character varying(100) NOT NULL,
    country character varying(100) NOT NULL,
    user_id integer
);
    DROP TABLE public.address;
       public         heap r       postgres    false    4            �            1259    16434    address_id_seq    SEQUENCE     �   CREATE SEQUENCE public.address_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.address_id_seq;
       public               postgres    false    222    4            P           0    0    address_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.address_id_seq OWNED BY public.address.id;
          public               postgres    false    221            �            1259    16390    authors    TABLE     �   CREATE TABLE public.authors (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    nationality character varying(100) NOT NULL,
    birthday date NOT NULL,
    place_of_birth character varying(255) NOT NULL
);
    DROP TABLE public.authors;
       public         heap r       postgres    false    4            �            1259    16389    authors_id_seq    SEQUENCE     �   CREATE SEQUENCE public.authors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.authors_id_seq;
       public               postgres    false    218    4            Q           0    0    authors_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.authors_id_seq OWNED BY public.authors.id;
          public               postgres    false    217            �            1259    16399    books    TABLE     |  CREATE TABLE public.books (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    price numeric(10,2) NOT NULL,
    quantity integer NOT NULL,
    author_id integer NOT NULL,
    year_of_publication integer NOT NULL,
    CONSTRAINT books_quantity_check CHECK ((quantity >= 0)),
    CONSTRAINT books_year_of_publication_check CHECK ((year_of_publication > 0))
);
    DROP TABLE public.books;
       public         heap r       postgres    false    4            �            1259    16398    books_id_seq    SEQUENCE     �   CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.books_id_seq;
       public               postgres    false    4    220            R           0    0    books_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;
          public               postgres    false    219            �            1259    16444    users    TABLE       CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    password_hash text NOT NULL,
    address_id integer,
    place_of_birth character varying(255) NOT NULL,
    birthday_date date NOT NULL
);
    DROP TABLE public.users;
       public         heap r       postgres    false    4            �            1259    16443    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public               postgres    false    4    224            S           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public               postgres    false    223            �           2604    16438 
   address id    DEFAULT     h   ALTER TABLE ONLY public.address ALTER COLUMN id SET DEFAULT nextval('public.address_id_seq'::regclass);
 9   ALTER TABLE public.address ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    221    222    222            �           2604    16393 
   authors id    DEFAULT     h   ALTER TABLE ONLY public.authors ALTER COLUMN id SET DEFAULT nextval('public.authors_id_seq'::regclass);
 9   ALTER TABLE public.authors ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    218    217    218            �           2604    16402    books id    DEFAULT     d   ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);
 7   ALTER TABLE public.books ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    219    220    220            �           2604    16447    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    224    223    224            F          0    16435    address 
   TABLE DATA           E   COPY public.address (id, street, city, country, user_id) FROM stdin;
    public               postgres    false    222   �,       B          0    16390    authors 
   TABLE DATA           R   COPY public.authors (id, name, nationality, birthday, place_of_birth) FROM stdin;
    public               postgres    false    218   -       D          0    16399    books 
   TABLE DATA           [   COPY public.books (id, title, price, quantity, author_id, year_of_publication) FROM stdin;
    public               postgres    false    220   `-       H          0    16444    users 
   TABLE DATA           j   COPY public.users (id, name, email, password_hash, address_id, place_of_birth, birthday_date) FROM stdin;
    public               postgres    false    224   }-       T           0    0    address_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.address_id_seq', 1, false);
          public               postgres    false    221            U           0    0    authors_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.authors_id_seq', 1, true);
          public               postgres    false    217            V           0    0    books_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.books_id_seq', 2, true);
          public               postgres    false    219            W           0    0    users_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.users_id_seq', 1, false);
          public               postgres    false    223            �           2606    16440    address address_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.address DROP CONSTRAINT address_pkey;
       public                 postgres    false    222            �           2606    16442    address address_user_id_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_user_id_key UNIQUE (user_id);
 E   ALTER TABLE ONLY public.address DROP CONSTRAINT address_user_id_key;
       public                 postgres    false    222            �           2606    16397    authors authors_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.authors
    ADD CONSTRAINT authors_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.authors DROP CONSTRAINT authors_pkey;
       public                 postgres    false    218            �           2606    16406    books books_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.books DROP CONSTRAINT books_pkey;
       public                 postgres    false    220            �           2606    16455    users users_address_id_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_address_id_key UNIQUE (address_id);
 D   ALTER TABLE ONLY public.users DROP CONSTRAINT users_address_id_key;
       public                 postgres    false    224            �           2606    16453    users users_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public.users DROP CONSTRAINT users_email_key;
       public                 postgres    false    224            �           2606    16451    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public                 postgres    false    224            �           2606    16461    address fk_address_user    FK CONSTRAINT     �   ALTER TABLE ONLY public.address
    ADD CONSTRAINT fk_address_user FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;
 A   ALTER TABLE ONLY public.address DROP CONSTRAINT fk_address_user;
       public               postgres    false    3244    222    224            �           2606    16407    books fk_books_author    FK CONSTRAINT     �   ALTER TABLE ONLY public.books
    ADD CONSTRAINT fk_books_author FOREIGN KEY (author_id) REFERENCES public.authors(id) ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.books DROP CONSTRAINT fk_books_author;
       public               postgres    false    3232    220    218            �           2606    16456    users fk_users_address    FK CONSTRAINT     �   ALTER TABLE ONLY public.users
    ADD CONSTRAINT fk_users_address FOREIGN KEY (address_id) REFERENCES public.address(id) ON DELETE SET NULL;
 @   ALTER TABLE ONLY public.users DROP CONSTRAINT fk_users_address;
       public               postgres    false    224    3236    222            F      x������ � �      B   =   x�3�����S�/���K�t*�,�,��4�43�50�56�L,I�Qp�K�I�K����� ��b      D      x������ � �      H      x������ � �     